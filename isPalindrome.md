### Kiểm tra số Palindrome

Hãy tưởng tượng bạn có một số và bạn muốn biết liệu số đó có phải là số Palindrome hay không. Một số Palindrome là số mà khi đọc ngược lại vẫn giống như khi đọc xuôi.

### Cách kiểm tra số Palindrome:

Chúng ta sẽ chuyển số đó thành chuỗi (string) và sau đó so sánh chuỗi này với phiên bản đảo ngược của nó. Nếu hai chuỗi này giống nhau, thì số đó là số Palindrome.

## Các bước thực hiện:

1. **Chuyển số thành chuỗi:**

   - Chuyển số thành chuỗi để có thể dễ dàng so sánh các ký tự.

2. **Đảo ngược chuỗi:**

   - Tạo một chuỗi mới là phiên bản đảo ngược của chuỗi ban đầu.

3. **So sánh chuỗi ban đầu và chuỗi đảo ngược:**

   - Nếu hai chuỗi này giống nhau, thì số đó là số Palindrome.
   - Nếu hai chuỗi này khác nhau, thì số đó không phải là số Palindrome.

## Ví dụ:

Giả sử bạn có số `121` và bạn muốn kiểm tra xem nó có phải là số Palindrome hay không.

- **Bước 1:** Chuyển số `121` thành chuỗi `"121"`.
- **Bước 2:** Đảo ngược chuỗi `"121"` để có chuỗi `"121"`.
- **Bước 3:** So sánh chuỗi `"121"` và chuỗi `"121"`. Vì chúng giống nhau, nên số `121` là số Palindrome.

Giả sử bạn có số `123` và bạn muốn kiểm tra xem nó có phải là số Palindrome hay không.

- **Bước 1:** Chuyển số `123` thành chuỗi `"123"`.
- **Bước 2:** Đảo ngược chuỗi `"123"` để có chuỗi `"321"`.
- **Bước 3:** So sánh chuỗi `"123"` và chuỗi `"321"`. Vì chúng khác nhau, nên số `123` không phải là số Palindrome.

### Tại sao cách này hiệu quả?

Bằng cách chuyển số thành chuỗi và so sánh với phiên bản đảo ngược của nó, chúng ta có thể dễ dàng kiểm tra xem số đó có phải là số Palindrome hay không mà không cần phải thực hiện các phép tính phức tạp.