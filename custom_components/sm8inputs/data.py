import lib8inputs

FULL_NAME = "Eight HV Digital Inputs"
LINK = (
    "https://sequentmicrosystems.com/products/eight-hv-digital-inputs-for-raspberry-pi"
)
API = lib8inputs
DOMAIN = "sm8inputs"
NAME_PREFIX = "sm8i"
SM_MAP = {
    "binary_sensor": {
        "opto": {
            "chan_no": 8,
            "com": {
                "get": "get_opto",
            },
        },
    },
}
