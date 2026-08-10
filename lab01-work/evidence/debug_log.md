## Record the exception type and message from the final traceback line.

![error output](error_output.png)]

## Name the top-level entry file and line.

![error output](error_output.png)]

## Identify the first location in your own code that should be inspected.

 print(format_student_record("Lin", "eighty"))

## Classify the failure as environment, syntax, type, value, or logic—and explain why.

type error，"eighty" isn't an integer

## Use the contract to argue whether responsibility belongs at the caller or function boundary.

因為caller違反了score應該是int型態的條件，所以修復這個問題的責任落在caller（應該改成傳入數字 80）。函式內部拋出TypeError是非常正確的行為，它成功守住了自己的邊界，防止錯誤的資料繼續往下流竄。