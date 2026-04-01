import pytest
from unittest.mock import Mock
from main import BankAccount


@pytest.fixture
def account():
    mock_logger = Mock()
    acc = BankAccount(balance=100, logger=mock_logger)
    return acc, mock_logger


def test_deposit_normal(account):
    acc, mock_logger = account
    acc.deposit(50)
    assert acc.balance == 150
    mock_logger.log.assert_called_once_with("Deposited 50")



def test_withdraw_normal(account):
    acc, mock_logger = account
    acc.withdraw(40)
    assert acc.balance == 60
    mock_logger.log.assert_called_once_with("Withdrew 40")



def test_deposit_zero(account):
    acc, mock_logger = account
    acc.deposit(0)
    assert acc.balance == 100
    mock_logger.log.assert_called_once_with("Deposited 0")


def test_withdraw_exact_balance(account):
    acc, mock_logger = account
    acc.withdraw(100)
    assert acc.balance == 0
    mock_logger.log.assert_called_once_with("Withdrew 100")



def test_withdraw_insufficient_funds(account):
    acc, mock_logger = account
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(500)
    mock_logger.log.assert_called_once_with("Failed withdrawal of 500")
