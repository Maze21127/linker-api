from app.models import Url, db, Group


def create_link(source_link: str,  redirect_link: str, group=str | None):
    group_id = Group.query.filter_by(name=group).first().id if group else None
    try:
        link = Url(link=redirect_link, real_link=source_link, group_id=group_id)
        db.session.add(link)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False
