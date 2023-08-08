from fpdf import FPDF
import pandas as pd

df = pd.read_csv("app11-hotelbooking/challenge1/articles.csv", dtype={"id": str})


class Buying:
    def __init__(self, item_id):
        self.id = item_id
        self.name = df.loc[df["id"] == self.item_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.item_id, "price"].squeeze()

    def update(self):
        df.loc[df["id"] == self.id, "in stock"] = df.loc[df["id"] == self.id, "in stock"].squeeze() - 1
        df.to_csv("app11-hotelbooking/challenge1/articles.csv", index=False)


class PDF(FPDF):
    PDF = FPDF(orientation="P", unit="mm", format="A4")
    def __init__(self, number, article, price):
        self.number = number
        self.article = article
        self.price = price
        self.PDF.add_page()

    def generate(self):
        self.PDF.set_font(family="Times", size=16, style="B")
        self.PDF.cell(w=50, h=8, txt=f"Receipt nr. {self.number}", ln=1)

        self.PDF.set_font(family="Times", size=16, style="B")
        self.PDF.cell(w=50, h=8, txt=f"Article: {self.article}", ln=1)

        self.PDF.set_font(family="Times", size=16, style="B")
        self.PDF.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        return self.PDF.output("app11-hotelbooking/challenge1/receipt.pdf")


if __name__ == "__main__":
    print(df)
    item_id = input("Choose an article to buy: ")
    buy = Buying(item_id=item_id)
    pdf = PDF(number=buy.id, article=buy.name, price=buy.price)
    pdf.generate()
    buy.update()




