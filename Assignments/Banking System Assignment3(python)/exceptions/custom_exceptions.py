class InvalidAccountException(Exception):
    def __init__(self, message="The account number entered is invalid or does not exist."):
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in the account to complete the transaction."):
        super().__init__(message)


class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Withdrawal amount exceeds the overdraft limit."):
        super().__init__(message)
