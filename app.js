// Configuration for VietQR (Napas247) - 100% Free, direct to bank account
// Người dùng có thể thay đổi số tài khoản & ngân hàng trong file này mà không mất 1 đồng phí
const PAYMENT_CONFIG = {
  bankId: "970423", // TPBank (Ngân hàng TMCP Tiên Phong)
  accountNo: "20058999999", // Số tài khoản TPBank của bạn
  accountName: "", // VietQR tự động tra cứu tên chủ tài khoản TPBank
  template: "compact2", // Giao diện chuẩn Napas247
  defaultMemo: "SOLO2026"
};

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

    // Tạo mã VietQR động
    const qrUrl = `https://img.vietqr.io/image/${PAYMENT_CONFIG.bankId}-${PAYMENT_CONFIG.accountNo}-${PAYMENT_CONFIG.template}.png?amount=${amount}&addInfo=${PAYMENT_CONFIG.defaultMemo}&accountName=${encodeURIComponent(PAYMENT_CONFIG.accountName)}`;
    
    document.getElementById('vietQrImg').src = qrUrl;
    document.getElementById('modalAmountText').innerText = amount.toLocaleString('vi-VN') + ' VNĐ';
    document.getElementById('modalMemoText').innerText = PAYMENT_CONFIG.defaultMemo;

    Tracker.logEvent('open_vietqr_checkout', { amount: amount });
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

// Đóng modal khi click ra ngoài vùng nội dung
window.onclick = function(event) {
  const modal = document.getElementById('checkoutModal');
  if (event.target === modal) {
    closeCheckoutModal();
  }
};
