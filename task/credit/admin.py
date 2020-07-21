from django.contrib import admin
from credit.models import (
    Request,
    Borrower,
    BlockedTarget,
    CreditProgramm,
)


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    pass


@admin.register(CreditProgramm)
class CreditProgrammAdmin(admin.ModelAdmin):
    pass


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass


@admin.register(BlockedTarget)
class BlockedTargetAdmin(admin.ModelAdmin):
    pass
