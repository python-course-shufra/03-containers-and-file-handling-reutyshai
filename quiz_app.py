import sys
import random


def main():
    # TODO: your code here
    args=sys.argv
    with open(f"questions//{args[1]}.txt") as quiz:
            sum_unswers=int(args[2])
            for line in quiz:
                parts=line.split(";")
                print(parts[0])
                option=parts[2].split(",")
                option.append(parts[1])
                res,count_res=parts[1],0
                random.shuffle(option)
                for i,item in enumerate(option):
                    print(f"{i+1}. {item}")
                x=int(input("select the correct answer: "))
                if option[x-1]==res:
                    count_res+=1
                sum_unswers-=1
                if int(sum_unswers==0):
                    break
            print(f"you answered {count_res}/{args[2]} answers")
    # 1. Get the command line arguments via sys.argv

    # 2. Open the correct file open(rf'questions\<filename>.txt)'

    # 3. Iterate over the file

    #       3.1. Parse the line (use s.split())
    #       3.2 Create a list of options
    #       3.3 random.shuffle(l)
    pass


if __name__ == '__main__':
    main()
