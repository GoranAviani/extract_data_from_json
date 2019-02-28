import json



def main():
    file = open("result.txt", "w")



    with open("get_tel.txt", "r", encoding="utf-8") as fin:
        lineNo = 0

        for line in fin:
            lineNo += 1

            #dataform = rsq.read().decode().replace('\n','')
            #jsonLine = json.loads(dataform)

            #if json.loads(line) == '':
            #    pass
            #else:
            #    jsonLine = json.loads(line)
            jsonLine = json.loads(line)
            print (jsonLine)
            print(str(lineNo))
            print(jsonLine["telefonnummer"])
            file.write(jsonLine["telefonnummer"])
            file.write("\n")

    file.close()


if __name__ == "__main__":
    main()