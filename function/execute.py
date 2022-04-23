import atexit
import mintapi

EMAIL = "burkematthewjoseph@gmail.com"


def lambda_handler(event, context):
    password = "test"
    imap_password = "test"

    mint = mintapi.Mint(
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
