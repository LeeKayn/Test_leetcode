### Tưởng tượng một cuộc thi đoán số

Hãy tưởng tượng bạn đang chơi một trò chơi đoán số. Có một danh sách các số được sắp xếp theo thứ tự tăng dần, và nhiệm vụ của bạn là tìm một số cụ thể trong danh sách đó.

### Cách chơi thông minh:

Thay vì kiểm tra từng số một từ đầu đến cuối, chúng ta sẽ sử dụng phương pháp tìm kiếm nhị phân. Phương pháp này giống như khi bạn chơi trò đoán số, bạn sẽ đoán một số ở giữa để thu hẹp phạm vi tìm kiếm.

## Các bước thực hiện:

1. **Tìm số ở giữa:**

   - Nhìn vào số ở giữa danh sách.
   - So sánh số ở giữa với số bạn muốn tìm.

2. **So sánh và quyết định:**

   - Nếu số ở giữa bằng số bạn muốn tìm, bạn đã tìm thấy số đó.
   - Nếu số ở giữa nhỏ hơn số bạn muốn tìm, số bạn cần tìm sẽ nằm ở nửa bên phải của danh sách.
   - Nếu số ở giữa lớn hơn số bạn muốn tìm, số bạn cần tìm sẽ nằm ở nửa bên trái của danh sách.

3. **Tiếp tục tìm kiếm:**

   - Tập trung vào nửa danh sách mà số bạn cần tìm có thể nằm ở đó.
   - Lặp lại bước 1 và 2 với nửa danh sách mới này.
   - Tiếp tục quá trình này cho đến khi tìm thấy số bạn muốn tìm hoặc khi không còn số nào để tìm nữa.

## Ví dụ:

Giả sử bạn có danh sách các số: `[2, 5, 8, 12, 15, 19, 22]` và bạn muốn tìm số `15`.

- **Bước 1:** Số ở giữa là `12`. Vì `12` nhỏ hơn `15`, nên ta sẽ tìm ở nửa bên phải.
- **Bước 2:** Bây giờ danh sách của chúng ta là `[15, 19, 22]`. Số ở giữa là `19`. Vì `19` lớn hơn `15`, nên ta sẽ tìm ở nửa bên trái của danh sách này.
- **Bước 3:** Danh sách còn lại chỉ có một số là `15`. Và đây chính là số chúng ta đang tìm!

### Tại sao tìm kiếm nhị phân lại nhanh?

Mỗi lần tìm kiếm, chúng ta loại bỏ được một nửa danh sách. Điều này giúp chúng ta tìm thấy kết quả rất nhanh, đặc biệt là khi danh sách rất lớn.

Giống như khi bạn tìm một từ trong từ điển. Bạn sẽ không lật từng trang một mà sẽ mở ra giữa từ điển và so sánh.

Vậy là chúng ta đã hiểu được thuật toán tìm kiếm nhị phân rồi đấy!