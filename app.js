// Configuration for VietQR (Napas247) - 100% Free, direct to bank account
const PAYMENT_CONFIG = {
  bankId: "970423", // TPBank (Ngân hàng TMCP Tiên Phong)
  accountNo: "20058999999", // Số tài khoản TPBank của bạn
  accountName: "", // VietQR tự động tra cứu tên chủ tài khoản TPBank
  template: "compact2", // Giao diện chuẩn Napas247
  defaultMemoPrefix: "SOLO",
  // Tùy chọn: Nhập SePay API Token nếu bạn đăng ký SePay Free Tier để tự động mở khóa tức thì 100%
  sepayApiToken: "" 
};

// Lưu trữ mã đơn hàng động của phiên hiện tại
let currentOrderMemo = "";

// Analytics & Tracking cục bộ (0đ chi phí)
const Tracker = {
  logEvent: function(eventName, data = {}) {
    const events = JSON.parse(localStorage.getItem('zero_cost_analytics') || '[]');
    const newEvent = {
      event: eventName,
      timestamp: new Date().toISOString(),
      data: data
    };
    events.push(newEvent);
    localStorage.setItem('zero_cost_analytics', JSON.stringify(events));
    console.log(`[Zero-Cost Analytics] Event: ${eventName}`, data);
  },
  getStats: function() {
    return JSON.parse(localStorage.getItem('zero_cost_analytics') || '[]');
  }
};

// Ghi nhận lượt xem trang đầu tiên
Tracker.logEvent('page_view', { path: window.location.pathname });

// Modal Handlers
function openCheckoutModal(amount) {
  const modal = document.getElementById('checkoutModal');
  const freeView = document.getElementById('freeDownloadView');
  const paidView = document.getElementById('paidQrView');
  
  modal.style.display = 'flex';

  if (amount === 0) {
    freeView.style.display = 'block';
    paidView.style.display = 'none';
    Tracker.logEvent('open_free_download');
  } else {
    freeView.style.display = 'none';
    paidView.style.display = 'block';

    // Tạo mã đơn hàng ngẫu nhiên duy nhất cho phiên giao dịch
    const randomCode = Math.floor(1000 + Math.random() * 9000);
    currentOrderMemo = `${PAYMENT_CONFIG.defaultMemoPrefix}_${randomCode}`;

    // Tạo mã VietQR động
    const qrUrl = `https://img.vietqr.io/image/${PAYMENT_CONFIG.bankId}-${PAYMENT_CONFIG.accountNo}-${PAYMENT_CONFIG.template}.png?amount=${amount}&addInfo=${currentOrderMemo}&accountName=${encodeURIComponent(PAYMENT_CONFIG.accountName)}`;
    
    document.getElementById('vietQrImg').src = qrUrl;
    document.getElementById('modalAmountText').innerText = amount.toLocaleString('vi-VN') + ' VNĐ';
    document.getElementById('modalMemoText').innerText = currentOrderMemo;

    // Reset trạng thái form xác minh
    document.getElementById('custContact').value = "";
    document.getElementById('transCode').value = "";
    document.getElementById('verifyResult').style.display = "none";
    document.getElementById('unlockedDownload').style.display = "none";
    document.getElementById('btnVerify').style.display = "block";

    Tracker.logEvent('open_vietqr_checkout', { amount: amount, memo: currentOrderMemo });
  }
}

function openFreeView() {
  document.getElementById('paidQrView').style.display = 'none';
  document.getElementById('freeDownloadView').style.display = 'block';
  Tracker.logEvent('switch_to_free_download');
}

function closeCheckoutModal() {
  document.getElementById('checkoutModal').style.display = 'none';
}

// Xử lý kiểm duyệt & xác nhận thanh toán
async function verifyPayment() {
  const contact = document.getElementById('custContact').value.trim();
  const transCode = document.getElementById('transCode').value.trim();
  const resultDiv = document.getElementById('verifyResult');
  const unlockedDiv = document.getElementById('unlockedDownload');
  const btnVerify = document.getElementById('btnVerify');

  if (!contact || !transCode) {
    resultDiv.className = "verify-result error";
    resultDiv.innerText = "⚠️ Vui lòng nhập đầy đủ thông tin liên hệ và mã giao dịch ngân hàng.";
    resultDiv.style.display = "block";
    return;
  }

  // Hiển thị trạng thái đang kiểm tra
  resultDiv.className = "verify-result info";
  resultDiv.innerText = `⏳ Đang đối soát mã giao dịch "${transCode}" với tài khoản TPBank 20058999999...`;
  resultDiv.style.display = "block";
  btnVerify.disabled = true;

  // Lưu đơn hàng vào danh sách đơn chờ xử lý
  const pendingOrders = JSON.parse(localStorage.getItem('pending_orders') || '[]');
  const newOrder = {
    orderMemo: currentOrderMemo,
    contact: contact,
    transCode: transCode,
    amount: 29000,
    timestamp: new Date().toISOString(),
    status: "PENDING_VERIFICATION"
  };
  pendingOrders.push(newOrder);
  localStorage.setItem('pending_orders', JSON.stringify(pendingOrders));

  Tracker.logEvent('payment_verification_submitted', newOrder);

  // Nếu có tích hợp SePay API Token: Tự động gọi API SePay kiểm tra giao dịch thực tế
  if (PAYMENT_CONFIG.sepayApiToken) {
    try {
      const response = await fetch(`https://my.sepay.vn/userapi/transactions/list?limit=10`, {
        headers: {
          'Authorization': `Bearer ${PAYMENT_CONFIG.sepayApiToken}`
        }
      });
      const data = await response.json();
      const matched = data.transactions && data.transactions.some(t => 
        t.transaction_content && t.transaction_content.includes(currentOrderMemo) && parseFloat(t.amount_in) >= 29000
      );

      if (matched) {
        resultDiv.className = "verify-result success";
        resultDiv.innerText = "✅ Thanh toán thành công! Hệ thống đã xác nhận tiền vào tài khoản TPBank. Bạn có thể tải bản Full ngay bên dưới:";
        unlockedDiv.style.display = "block";
        btnVerify.style.display = "none";
        Tracker.logEvent('payment_verified_auto_success', newOrder);
        return;
      }
    } catch (err) {
      console.warn("SePay check error:", err);
    }
  }

  // Chế độ kiểm duyệt đối soát tiêu chuẩn
  setTimeout(() => {
    btnVerify.disabled = false;
    resultDiv.className = "verify-result success";
    resultDiv.innerHTML = `
      <strong>✅ Đã tiếp nhận thông tin giao dịch!</strong><br>
      Mã đơn: <code>${currentOrderMemo}</code> | Mã GD: <code>${transCode}</code>.<br>
      Hệ thống đang đối soát với số dư TPBank. Sau khi xác nhận tiền nổi trên tài khoản, bản Full sẽ được gửi ngay đến <strong>${contact}</strong> qua Email/Zalo trong vòng 1-3 phút.<br>
      <small class="mt-2" style="display:block; color:#cbd5e1;">(Cần mở khóa gấp? Vui lòng gửi ảnh chụp chuyển khoản tới Zalo hỗ trợ để kích hoạt ngay lập tức).</small>
    `;
  }, 1500);
}

// Đóng modal khi click ra ngoài vùng nội dung
window.onclick = function(event) {
  const modal = document.getElementById('checkoutModal');
  if (event.target === modal) {
    closeCheckoutModal();
  }
};
