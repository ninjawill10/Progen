line = 0
variables = {}
output = []

with open("./main.Pg", "r") as file:
  commands = file.readlines()
  for command in commands:
    line += 1
    tokens = command.strip().split()
    if len(tokens) > 2 and tokens[1] == "=":
      variable_name = tokens[0]
      variable_value = " ".join(tokens[2:])
      variables[variable_name] = variable_value
    elif tokens[0] == "write":
      if len(tokens) > 1:
        output_values = []
        for token in tokens[1:]:
          if token.startswith("$"):
            variable_name = token[1:]
            if variable_name in variables:
              output_values.append(variables[variable_name])
            else:
              output_values.append(
                f"Error: Variable '{variable_name}' not found")
          else:
            output_values.append(token)
        print(" ".join(output_values))
      else:
        print("Invalid write statement")
    elif tokens[0] == "input":
      variable_name = tokens[1]
      user_input = input()
      variables[variable_name] = user_input
    else:
      print(f"Invalid Command at line {line}")