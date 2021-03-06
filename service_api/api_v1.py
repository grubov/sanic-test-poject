from sanic import Blueprint, Sanic

from resources.contracts import ContractResource, ContractsResource
from resources.payments import PaymentResource, PaymentsResource
from resources.smoke import SmokeResource
from service_api.constants import SERVICE_NAME


def load_api(app: Sanic):
    api_v1 = Blueprint('v1', url_prefix=f'/{SERVICE_NAME}/v1', strict_slashes=False)

    api_v1.add_route(ContractResource.as_view(), "/contracts/<contract_id:int>", strict_slashes=False)
    api_v1.add_route(ContractsResource.as_view(), "/contracts", strict_slashes=False)
    api_v1.add_route(PaymentResource.as_view(),
                     "/contracts/<contract_id:int>/payments/<payment_id:int>", strict_slashes=False)
    api_v1.add_route(PaymentsResource.as_view(), "/contracts/<contract_id:int>/payments", strict_slashes=False)
    api_v1.add_route(SmokeResource.as_view(), "/smoke", strict_slashes=False)

    app.blueprint(api_v1)
