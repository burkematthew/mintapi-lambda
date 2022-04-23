import atexit
import keyring
from mintapi import Mint

EMAIL = "burkematthewjoseph@gmail.com"


def lambda_handler(event, context):
    password = keyring.get_password("mintapi", EMAIL)
    imap_password = keyring.get_password("mintapi_imap", EMAIL)

    mint = Mint(
        EMAIL,
        password,
        mfa_method="email",
        imap_server="imap.gmail.com",
        imap_account=EMAIL,
        imap_password=imap_password,
        headless=True,
    )
    atexit.register(mint.close)  # Ensure everything is torn down.

    investments = mint.get_investment_data()
    return investments
