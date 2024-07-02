import argparse
import random
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.units import inch

def read_items(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def generate_bingo_card(items):
    return random.sample(items, 25)

def create_bingo_pdf(cards, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    elements = []

    for card in cards:
        data = [card[i:i+5] for i in range(0, 25, 5)]
        data[2][2] = "FREE"  # Center square is always FREE
        
        table = Table(data, colWidths=[1.2*inch]*5, rowHeights=[1.2*inch]*5)
        table.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 14),
            ('BACKGROUND', (2,2), (2,2), colors.lightgrey),  # FREE space
        ]))
        
        elements.append(table)
        elements.append(PageBreak())

    doc.build(elements)

def main():
    parser = argparse.ArgumentParser(description="Generate Bingo Cards")
    parser.add_argument("input_file", help="Path to the file containing bingo items")
    parser.add_argument("num_cards", type=int, help="Number of unique bingo cards to generate")
    parser.add_argument("output_file", help="Path to the output PDF file")
    args = parser.parse_args()

    items = read_items(args.input_file)
    if len(items) < 24:  # We need at least 24 items (25th is FREE)
        print("Error: Input file must contain at least 24 items.")
        return

    cards = [generate_bingo_card(items) for _ in range(args.num_cards)]
    create_bingo_pdf(cards, args.output_file)
    print(f"{args.num_cards} bingo cards have been generated and saved to {args.output_file}")

if __name__ == "__main__":
    main()
