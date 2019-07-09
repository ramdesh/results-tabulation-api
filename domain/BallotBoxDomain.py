from config import db
from models import BallotBoxModel as Model
from domain import InvoiceItemDomain


def get_all():
    result = Model.query.all()

    return result


def create(body):
    invoice_item = InvoiceItemDomain.create()
    result = Model(
        ballotBoxId=body["ballotBoxId"],
        invoiceItemId=invoice_item.invoiceItemId
    )

    db.session.add(result)
    db.session.commit()

    return result