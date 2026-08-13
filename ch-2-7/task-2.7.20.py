from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Integer


class Base(DeclarativeBase):
    pass

class GeoShape(Base):
    __tablename__ = "geo_shapes"

    id: Mapped[int] = mapped_column(primary_key=True)
    shape_kind: Mapped[str] = mapped_column(String(20), nullable=False)  # дискриминатор
    tag: Mapped[str] = mapped_column(String(40), nullable=False)

    __mapper_args__ = {
        "polymorphic_on": shape_kind,
        "polymorphic_identity": "shape",
    }


# Напишите ваш код тут
class CircleShape(GeoShape):
    __tablename__ = "geo_circles"
    id: Mapped[int] = mapped_column(ForeignKey("geo_shapes.id"), primary_key=True)
    radius_m: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "circle",
    }


class RectShape(GeoShape):
    __tablename__ = "geo_rects"
    id: Mapped[int] = mapped_column(ForeignKey("geo_shapes.id"), primary_key=True)
    width_m: Mapped[int] = mapped_column(Integer, nullable=False)
    height_m: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "rect",
    }
