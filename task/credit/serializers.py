from rest_framework import serializers, exceptions
from credit.models import Request
from credit.tests import (
    create_borrower,
    check_amount,
    check_age,
    check_target,
    check_in_black_list
)


class RequestSerializer(serializers.ModelSerializer):
    iin = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Request
        fields = "__all__"
        extra_kwargs = {
            'status': {'read_only': True},
            'rejection_reason': {'read_only': True},
            'borrower': {'read_only': True},
        }

    def create(self, validated_data):
        target = validated_data.pop('iin')
        borrower = create_borrower(target)
        programm_id = validated_data.get('programm').id
        amount = validated_data.get('amount')

        validated_data['borrower'] = borrower
        validated_data['status'] = Request.ACCEPTED

        call_check_amount = check_amount(programm_id=programm_id, amount=amount)
        if call_check_amount:
            validated_data['status'] = Request.DECLINED
            validated_data['rejection_reason'] = call_check_amount.get('message')

        call_check_age = check_age(programm_id=programm_id, age=borrower.age)
        if call_check_age:
            validated_data['status'] = Request.DECLINED
            validated_data['rejection_reason'] = call_check_age.get('message')

        call_check_target = check_target(target=target)
        if call_check_target:
            validated_data['status'] = Request.DECLINED
            validated_data['rejection_reason'] = call_check_target.get('message')

        call_check_in_black_list = check_in_black_list(target=target)
        if call_check_in_black_list:
            validated_data['status'] = Request.DECLINED
            validated_data['rejection_reason'] = call_check_in_black_list.get('message')

        return super().create(validated_data)
