from adapters.db.HelpDesk import HelpDesk
from sqlmodel import Session, select


class HelpDeskService:
    def __init__(self) -> None:
        pass

    async def add_helpdesk(self, hd: HelpDesk = None, db: Session = None):
        dict_hd = hd.dict()
        db.add(HelpDesk(**dict_hd))
        db.commit()
        return hd

    def get_helpdesk(self, db: Session = None):
        query = select(HelpDesk)
        result = db.exec(query.order_by(HelpDesk.created_at.desc())).all()
        return result
