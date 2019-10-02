from typing import Set

from app import db
from auth import authorize
from auth.AuthConstants import ALL_ROLES
from exception import NotFoundException
from orm.entities.Submission import TallySheet
from orm.entities.Submission.TallySheet import Model as TallySheetModel
from orm.entities.SubmissionVersion import TallySheetVersion
from schemas import TallySheetSchema
from util import RequestBody


@authorize(required_roles=ALL_ROLES)
def getAll(electionId=None, officeId=None, tallySheetCode=None):
    result = TallySheet.get_all(
        electionId=electionId,
        officeId=officeId,
        tallySheetCode=tallySheetCode
    )

    return TallySheetSchema(many=True).dump(result).data


@authorize(required_roles=ALL_ROLES)
def get_by_id(tallySheetId):
    tally_sheet = TallySheetModel.get_by_id(tallySheetId=tallySheetId)

    if tally_sheet is None:
        NotFoundException("Tally sheet not found (tallySheetId=%d)" % tallySheetId)

    return TallySheetSchema().dump(tally_sheet).data


def unlock(tallySheetId):
    tally_sheet = TallySheet.get_by_id(tallySheetId=tallySheetId)

    if tally_sheet is None:
        raise NotFoundException("Tally sheet not found (tallySheetId=%d)" % tallySheetId)

    tally_sheet.set_locked_version(None)

    db.session.commit()

    return TallySheetSchema().dump(tally_sheet).data, 201


def lock(tallySheetId, body):
    request_body = RequestBody(body)
    tallySheetVersionId = request_body.get("tallySheetVersionId")

    tally_sheet = TallySheet.get_by_id(tallySheetId=tallySheetId)

    if tally_sheet is None:
        raise NotFoundException("Tally sheet not found (tallySheetId=%d)" % tallySheetId)

    tally_sheet_version = TallySheetVersion.get_by_id(tallySheetVersionId=tallySheetVersionId)

    if tally_sheet_version is None:
        raise NotFoundException("Tally sheet version not found (tallySheetVersionId=%d)" % tallySheetVersionId)

    tally_sheet.set_locked_version(tally_sheet_version)

    db.session.commit()

    return TallySheetSchema().dump(tally_sheet).data, 201
