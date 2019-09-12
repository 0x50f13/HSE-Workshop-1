import argparse
import datetime
parser=argparse.ArgumentParser(description="HSE workshop program")

parser.add_argument('-b', "--birthday",
    help="Birthday - format YYYY-MM-DD",
    required=True,
    type=datetime.date.fromisoformat)
parser.add_argument('--name',type=str,required=True,help="Your name")

if __name__=='__main__':
   args=parser.parse_args()
   print("Delta(days):",datetime.date.today()-args.birthday)
   yrs=(datetime.date.today()-args.birthday).days//365
   print("Hello %s and you are %d years old"%(args.name,yrs))

   
