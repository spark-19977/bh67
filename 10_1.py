import pydantic
import csv


class EGE(pydantic.BaseModel):
    physics: int = pydantic.Field(le=100, ge=0)
    Informatics: int = pydantic.Field(le=100, ge=0)
    mathematics: int = pydantic.Field(le=100, ge=0)

    @classmethod
    def from_csv(cls, file):
        with open(file, 'r', encoding='utf-8') as fh:
            data = csv.DictReader(fh)
            return [EGE(**i) for i in data]

    def to_csv(self, file):
        with open(file, 'a+', encoding='utf-8', newline='') as fh:
            fields = self.dict()
            pos = fh.tell()
            fh.seek(0)
            data = fh.read()
            if data and not data.endswith('\n'):
                fh.write('\n')
            fh.seek(pos)
            writer = csv.DictWriter(fh, fields)
            if not fh.tell():
                writer.writeheader()
            writer.writerow(fields)


EGE_data = {
    "mathematics": 90,
    "physics": 70,
    "Informatics": 80
  }

EGE(**EGE_data)
print(a := EGE.from_csv('10_1.csv'))
a[0].to_csv('10_11.csv')