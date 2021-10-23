from samurai import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("read_user", values=dict(id="<id>")),
            "collection": ma.URLFor("read_users"),
        }
    )


user_serializer = UserSchema()
users_serializer = UserSchema(many=True)
