from fastmcp import FastMCP
from datetime import datetime


mcp = FastMCP("ramvillas")

@mcp.tool()
def current_date_time():
    """Return the current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


@mcp.tool()
def roll_dice():
    """Roll a six-sided dice."""
    import random
    return random.randint(1, 6)

@mcp.tool()
def generate_password(length: int = 12):
    """Generate a secure password."""
    import secrets
    import string

    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))

@mcp.tool()
def generate_qr(text: str) -> str:
    """Generate a QR code and save it as a PNG image."""
    import qrcode
    import os

    qr = qrcode.QRCode(border=2)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save to desktop or current folder
    path = os.path.join(os.getcwd(), "qrcode.png")
    img.save(path)

    return f"QR code saved at: {path}"   # LLM returns this path to user


if __name__ == "__main__":
    print("Starting MCP server..")
    mcp.run()

