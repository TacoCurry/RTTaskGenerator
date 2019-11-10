from TaskGen import GenTask
help = int(input("사용법(0:pass, 1:출력): "))

if help == 0:
    GenTask.makeTask()

elif help == 1:
    print("Usage: gasgen <options> <config path>\n"
          " <options>\n"
          "      -h: this message\n"
          "      -v: verbose mode\n")
    GenTask.makeTask()

