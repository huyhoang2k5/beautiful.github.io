# 🌐 HƯỚNG DẪN TRIỂN KHAI LANDING PAGE 0 ĐỒNG (FREE HOSTING)

Trang web này được xây dựng bằng công nghệ thuần túy (HTML5, CSS3, Vanilla JS), không cần máy chủ backend, không cần database và **hoàn toàn miễn phí 100% để lưu trữ trọn đời**.

---

## CÁCH 1: TRIỂN KHAI LÊN GITHUB PAGES (KHUYÊN DÙNG - 0 VNĐ)

1. Tạo một tài khoản GitHub miễn phí tại [github.com](https://github.com) (nếu chưa có).
2. Tạo một Repository mới, đặt tên tùy ý (ví dụ: `solopreneur-kit` hoặc `<username>.github.io`).
3. Tải toàn bộ các file trong thư mục `landing_page/` (`index.html`, `styles.css`, `app.js`) lên repository đó.
4. Vào phần **Settings** của repository -> Chọn **Pages** ở thanh bên trái.
5. Tại mục **Branch**, chọn `main` (hoặc `master`) và thư mục `/ (root)` -> Bấm **Save**.
6. Sau 1 phút, bạn sẽ nhận được đường dẫn trang web công khai miễn phí:
   `https://<username>.github.io/solopreneur-kit/`

---

## CÁCH 2: TRIỂN KHAI LÊN VERCEL (1-CLICK - 0 VNĐ)

1. Truy cập [vercel.com](https://vercel.com) và đăng nhập bằng tài khoản GitHub.
2. Bấm **Add New...** -> **Project** -> Chọn repository vừa tạo ở Bước 1.
3. Bấm **Deploy**.
4. Bạn sẽ có ngay một tên miền cực nhanh với SSL bảo mật miễn phí:
   `https://solopreneur-kit.vercel.app`

---

## CẤU HÌNH NHẬN TIỀN QUA VIETQR CỦA BẠN (0 ĐỒNG PHÍ)

Mở file `app.js` và chỉnh sửa thông tin ngân hàng của bạn tại mục `PAYMENT_CONFIG`:

```javascript
const PAYMENT_CONFIG = {
  bankId: "970423",          // TPBank (Ngân hàng TMCP Tiên Phong)
  accountNo: "20058999999",   // Số tài khoản TPBank của bạn
  accountName: "",           // VietQR tự động nhận diện chủ tài khoản
  template: "compact2",      // Giao diện chuẩn Napas247
  defaultMemo: "SOLO2026"     // Nội dung chuyển khoản
};
```

*Tiền của khách hàng chuyển sẽ về thẳng 100% vào tài khoản ngân hàng của bạn, không bị giam tiền, không mất phí chiết khấu cổng thanh toán!*
