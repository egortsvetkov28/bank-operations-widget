from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_transactions

print(get_mask_card_number("1234567890123456"))
print(get_mask_account("123456789012"))
print(load_transactions("test.json"))
