import os
from .cajparser import CAJParser
from .utils import add_outlines



def show_info(caj_path):
    caj = CAJParser(caj_path)
    if caj.format == "PDF" or caj.format == "KDH":
        print("File: {0}\nType: {1}\n".format(caj_path, caj.format))
    else:
        print("File: {0}\nType: {1}\nPage count: {2}\nOutlines count: {3}\n".format(
            caj_path,
            caj.format,
            caj.page_num,
            caj.toc_num
        ))

def convert_to_pdf(caj_path, output=None):
    caj = CAJParser(caj_path)
    if output is None:
        if caj_path.endswith(".caj"):
            output = caj_path.replace(".caj", ".pdf")
        elif (len(caj_path) > 4 and (caj_path[-4] == '.' or caj_path[-3] == '.') and not caj_path.endswith(".pdf")):
            output = os.path.splitext(caj_path)[0] + ".pdf"
        else:
            output = caj_path + ".pdf"
    caj.convert(output)

def extract_outlines(caj_path, output):
    caj = CAJParser(caj_path)
    if caj.format == "PDF" or caj.format == "KDH":
        raise SystemExit("Unsupported file type: {0}.".format(caj.format))
    toc = caj.get_toc()
    add_outlines(toc, output, "tmp.pdf")
    os.replace("tmp.pdf", output)

def extract_text(caj_path):
    caj = CAJParser(caj_path)
    caj.text_extract()

def parse_file(caj_path):
    caj = CAJParser(caj_path)
    caj.parse()




# import os
# import argparse
# from .cajparser import CAJParser
# from .utils import add_outlines

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     subparsers = parser.add_subparsers(help="commands", dest="command")

#     show_parser = subparsers.add_parser("show", help="Show the information of the CAJ file.")
#     show_parser.add_argument("input", help="Path to the CAJ file.")

#     convert_parser = subparsers.add_parser("convert", help="Convert the CAJ file to PDF file.")
#     convert_parser.add_argument("input", help="Path to the CAJ file.")
#     convert_parser.add_argument("-o", "--output", help="Output path to the PDF file.", required=False)

#     outlines_parser = subparsers.add_parser("outlines", help="Extract outlines from the CAJ file and add it to PDF file.")
#     outlines_parser.add_argument("input", help="Path to the CAJ file.")
#     outlines_parser.add_argument("-o", "--output", help="Path to the PDF file.", required=True)

#     parse_parser = subparsers.add_parser("parse", help="Parse CAJ file for debugging/development")
#     parse_parser.add_argument("input", help="Path to the CAJ file.")

#     text_extract_parser = subparsers.add_parser("text-extract", help="Parse CAJ file for debugging/development")
#     text_extract_parser.add_argument("input", help="Path to the CAJ file.")

#     args = parser.parse_args()

#     if args.command == "show":
#         caj = CAJParser(args.input)
#         if caj.format == "PDF" or caj.format == "KDH":
#             print("File: {0}\nType: {1}\n".format(args.input, caj.format))
#         else:
#             print("File: {0}\nType: {1}\nPage count: {2}\nOutlines count: {3}\n".format(
#                 args.input,
#                 caj.format,
#                 caj.page_num,
#                 caj.toc_num
#             ))

#     if args.command == "convert":
#         caj = CAJParser(args.input)
#         if args.output is None:
#             if args.input.endswith(".caj"):
#                 args.output = args.input.replace(".caj", ".pdf")
#             elif (len(args.input) > 4 and (args.input[-4] == '.' or args.input[-3] == '.') and not args.input.endswith(".pdf")):
#                 args.output = os.path.splitext(args.input)[0] + ".pdf"
#             else:
#                 args.output = args.input + ".pdf"
#         caj.convert(args.output)

#     if args.command == "outlines":
#         caj = CAJParser(args.input)
#         if caj.format == "PDF" or caj.format == "KDH":
#             raise SystemExit("Unsupported file type: {0}.".format(caj.format))
#         toc = caj.get_toc()
#         add_outlines(toc, args.output, "tmp.pdf")
#         os.replace("tmp.pdf", args.output)

#     if args.command == "text-extract":
#         caj = CAJParser(args.input)
#         caj.text_extract()

#     if args.command == "parse":
#         caj = CAJParser(args.input)
#         caj.parse()
















