// Questions Database
const questions = [
  {
    id: 1,
    text: "Khi nghe tin AI có thể làm thay 80% công việc văn phòng, phản ứng đầu tiên của bạn là gì?",
    options: [
      { text: "Nghiên cứu ngay cách dùng AI để tự động hóa 1 mô hình kinh doanh cá nhân.", archetype: "INNOVATOR" },
      { text: "Lập kế hoạch học cách quản lý và tối ưu hóa quy trình làm việc với chi phí tối thiểu.", archetype: "STRATEGIST" },
      { text: "Bắt đầu làm video, bài viết chia sẻ về công cụ AI mới để kéo người theo dõi.", archetype: "CREATOR" },
      { text: "Áp dụng ngay vào công việc freelance/kiếm tiền thêm ngoài giờ mỗi ngày.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 2,
    text: "Nếu được cấp 0 đồng vốn và 1 chiếc máy tính có internet, bạn sẽ bắt đầu bằng cách nào?",
    options: [
      { text: "Đóng gói 1 sản phẩm số (Templates, Prompts) và bán trên trang web miễn phí.", archetype: "INNOVATOR" },
      { text: "Nghiên cứu thị trường ngách có nhu cầu cao và tỷ lệ chuyển đổi tốt.", archetype: "STRATEGIST" },
      { text: "Làm kênh TikTok/Shorts/Threads chia sẻ kiến thức miễn phí thu hút tệp fan trung thành.", archetype: "CREATOR" },
      { text: "Nhận các công việc micro-task, bounty mã nguồn mở hoặc freelance kiếm tiền ngay.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 3,
    text: "Phong cách kiếm tiền nào khiến bạn cảm thấy hào hứng và bền vững nhất?",
    options: [
      { text: "Dòng tiền tự động hóa: Hệ thống làm việc và bán hàng kể cả khi tôi đang ngủ.", archetype: "INNOVATOR" },
      { text: "Hệ thống tối ưu: Rủi ro bằng 0, không lãng phí 1 đồng chi phí nào.", archetype: "STRATEGIST" },
      { text: "Kiếm tiền từ sức ảnh hưởng: Nội dung chạm đến cảm xúc và giải quyết vấn đề cho cộng đồng.", archetype: "CREATOR" },
      { text: "Thu nhập tăng theo tốc độ thực thi: Càng làm nhiều, kinh nghiệm và tiền càng tăng nhanh.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 4,
    text: "Bạn xử lý thời gian rảnh buổi tối (20h - 23h) như thế nào?",
    options: [
      { text: "Thử nghiệm các workflow AI mới và xây dựng hệ thống tự động.", archetype: "INNOVATOR" },
      { text: "Đọc sách, phân tích case study và tối ưu hóa tài chính cá nhân.", archetype: "STRATEGIST" },
      { text: "Lên kịch bản video, viết bài chia sẻ quan điểm trên mạng xã hội.", archetype: "CREATOR" },
      { text: "Cày cuốc hoàn thành dự án kiếm thêm tiền thật về tài khoản.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 5,
    text: "Mức độ chấp nhận thử nghiệm cái mới của bạn ra sao?",
    options: [
      { text: "Sẵn sàng là người tiên phong thử nghiệm các xu hướng AI mới nhất.", archetype: "INNOVATOR" },
      { text: "Chỉ thử khi đã có lộ trình rõ ràng và được kiểm chứng khả năng thành công.", archetype: "STRATEGIST" },
      { text: "Thử nghiệm ngay những định dạng nội dung độc lạ để xem phản ứng khán giả.", archetype: "CREATOR" },
      { text: "Không ngại vấp ngã, làm nhanh - sai nhanh - sửa nhanh.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 6,
    text: "Nếu một công cụ AI có thể kiếm ra 500.000đ/ngày hoàn toàn tự động, bạn sẽ làm gì tiếp theo?",
    options: [
      { text: "Nhân bản mô hình đó lên 5-10 nhánh khác nhau để mở rộng quy mô.", archetype: "INNOVATOR" },
      { text: "Tái cơ cấu dòng tiền, bảo vệ nguồn vốn và tối ưu biên lợi nhuận.", archetype: "STRATEGIST" },
      { text: "Làm một case study chia sẻ hành trình đó để truyền cảm hứng cho hàng ngàn người.", archetype: "CREATOR" },
      { text: "Tập trung khai thác tối đa công suất và tìm kiếm thêm các cơ hội khác.", archetype: "HUSTLER" }
    ]
  },
  {
    id: 7,
    text: "Mục tiêu lớn nhất của bạn trong 6-12 tháng tới là gì?",
    options: [
      { text: "Sở hữu 1 Solopreneur OS tự động tạo dòng tiền không cần quản lý thủ công.", archetype: "INNOVATOR" },
      { text: "Đạt sự tự do tài chính dựa trên các nguyên tắc quản trị tinh gọn.", archetype: "STRATEGIST" },
      { text: "Xây dựng thương hiệu cá nhân triệu view và cộng đồng 50.000 người theo dõi.", archetype: "CREATOR" },
      { text: "Tạo ra thu nhập online vượt mức lương văn phòng hiện tại.", archetype: "HUSTLER" }
    ]
  }
];

// Archetypes Profile Data
const archetypes = {
  INNOVATOR: {
    title: "AI Solopreneur Tiên Phong",
    subtitle: "The Visionary Innovator",
    badge: "🚀 TƯ DUY ĐỘT PHÁ - TIỀM NĂNG X10 THU NHẬP",
    tagline: "Bạn nhìn thấy cơ hội tự động hóa ở mọi ngóc ngách và có khả năng biến công nghệ AI thành dòng tiền thụ động.",
    strengths: ["Tư duy hệ thống vượt trội", "Thích ứng công nghệ cực nhanh", "Khả năng nhân bản quy mô cao"],
    bestModel: "Kinh doanh Sản Phẩm Số (Digital Products) & Micro-SaaS tự động hóa.",
    primaryColor: "#818cf8"
  },
  STRATEGIST: {
    title: "Chiến Lược Gia Tinh Gọn",
    subtitle: "The Lean Strategist",
    badge: "🎯 QUẢN TRỊ TỐI ƯU - RỦI RO 0 ĐỒNG",
    tagline: "Bạn có óc phân tích sắc bén, luôn biết cách kiếm tiền với chi phí thấp nhất và biên lợi nhuận cao nhất.",
    strengths: ["Kiểm soát rủi ro hoàn hảo", "Tối ưu hóa chi phí đến từng đồng", "Tầm nhìn dài hạn vững chắc"],
    bestModel: "Tiếp thị liên kết ngách (Affiliate) & Tư vấn giải pháp tự động hóa.",
    primaryColor: "#34d399"
  },
  CREATOR: {
    title: "Nhà Sáng Tạo Đa Năng",
    subtitle: "The Viral Creator",
    badge: "🎨 NẮM BẮT XU HƯỚNG - SỨC HÚT TRIỆU VIEW",
    tagline: "Bạn sở hữu trực giác tuyệt vời về nội dung và tâm lý con người, biến sự chú ý thành tài sản số sinh lời.",
    strengths: ["Kể chuyện lôi cuốn", "Bắt trend nhạy bén", "Xây dựng cộng đồng trung thành"],
    bestModel: "Sáng tạo nội dung TikTok/Threads & Bán tài nguyên số cho cộng đồng fan.",
    primaryColor: "#f472b6"
  },
  HUSTLER: {
    title: "Chiến Binh Thực Thi Bứt Phá",
    subtitle: "The Relentless Hustler",
    badge: "⚡ TỐC ĐỘ BÀN THỜ - BIẾN Ý TƯỞNG THÀNH TIỀN MẶT",
    tagline: "Bạn là người của hành động. Bạn không nói suông mà luôn bắt tay làm ngay để đem lại kết quả thực tế.",
    strengths: ["Tốc độ triển khai kinh ngạc", "Bền bỉ vượt qua khó khăn", "Học hỏi nhanh qua thực chiến"],
    bestModel: "Săn Bounties quốc tế, Freelance AI & Cung cấp dịch vụ số tốc độ cao.",
    primaryColor: "#fbbf24"
  }
};

let currentQuestionIndex = 0;
const scores = { INNOVATOR: 0, STRATEGIST: 0, CREATOR: 0, HUSTLER: 0 };
let currentResultArchetype = null;
let currentMemo = "";

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  renderQuestion();
});

function renderQuestion() {
  const q = questions[currentQuestionIndex];
  document.getElementById("question-counter").innerText = `Câu hỏi ${currentQuestionIndex + 1} / ${questions.length}`;
  const pct = Math.round(((currentQuestionIndex + 1) / questions.length) * 100);
  document.getElementById("progress-percent").innerText = `${pct}%`;
  document.getElementById("progress-fill").style.width = `${pct}%`;
  document.getElementById("question-text").innerText = q.text;

  const optionsGrid = document.getElementById("options-grid");
  optionsGrid.innerHTML = "";

  const letters = ["A", "B", "C", "D"];
  q.options.forEach((opt, idx) => {
    const btn = document.createElement("button");
    btn.className = "option-btn";
    btn.innerHTML = `<span class="option-letter">${letters[idx]}</span><span>${opt.text}</span>`;
    btn.onclick = () => selectOption(opt.archetype);
    optionsGrid.appendChild(btn);
  });
}

function selectOption(archetype) {
  scores[archetype] = (scores[archetype] || 0) + 1;
  currentQuestionIndex++;

  if (currentQuestionIndex < questions.length) {
    renderQuestion();
  } else {
    showResult();
  }
}

function showResult() {
  document.getElementById("quiz-screen").classList.add("hidden");
  document.getElementById("result-screen").classList.remove("hidden");

  // Determine top archetype
  let topArchetype = "INNOVATOR";
  let maxScore = -1;
  for (const [arch, score] of Object.entries(scores)) {
    if (score > maxScore) {
      maxScore = score;
      topArchetype = arch;
    }
  }

  currentResultArchetype = archetypes[topArchetype];
  document.getElementById("result-title").innerText = currentResultArchetype.title;
  document.getElementById("result-tagline").innerText = currentResultArchetype.tagline;

  // Draw Canvas Badge
  drawResultCanvas(currentResultArchetype);
}

function drawResultCanvas(arch) {
  const canvas = document.getElementById("result-canvas");
  const ctx = canvas.getContext("2d");

  // Background gradient
  const grad = ctx.createLinearGradient(0, 0, 600, 600);
  grad.addColorStop(0, "#0f172a");
  grad.addColorStop(0.5, "#1e1b4b");
  grad.addColorStop(1, "#090d14");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, 600, 600);

  // Border glow
  ctx.strokeStyle = "rgba(99, 102, 241, 0.4)";
  ctx.lineWidth = 4;
  ctx.strokeRect(16, 16, 568, 568);

  // Header Title
  ctx.fillStyle = "#94a3b8";
  ctx.font = "bold 16px 'Plus Jakarta Sans', sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("AI SOLOPRENEUR OS 2026 · PERSONALITY PROFILE", 300, 60);

  // Badge
  ctx.fillStyle = arch.primaryColor;
  ctx.font = "bold 14px 'Plus Jakarta Sans', sans-serif";
  ctx.fillText(arch.badge, 300, 95);

  // Big Archetype Title
  ctx.fillStyle = "#ffffff";
  ctx.font = "800 32px 'Plus Jakarta Sans', sans-serif";
  ctx.fillText(arch.title, 300, 150);

  ctx.fillStyle = "#c7d2fe";
  ctx.font = "italic 16px 'Plus Jakarta Sans', sans-serif";
  ctx.fillText(`“${arch.subtitle}”`, 300, 185);

  // Divider
  ctx.strokeStyle = "rgba(255, 255, 255, 0.1)";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(80, 215);
  ctx.lineTo(520, 215);
  ctx.stroke();

  // Strengths
  ctx.fillStyle = "#f8fafc";
  ctx.font = "bold 18px 'Plus Jakarta Sans', sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("THẾ MẠNH CỐT LÕI:", 80, 255);

  ctx.font = "16px 'Plus Jakarta Sans', sans-serif";
  ctx.fillStyle = "#cbd5e1";
  arch.strengths.forEach((st, idx) => {
    ctx.fillText(`✔  ${st}`, 90, 295 + idx * 35);
  });

  // Best Business Model
  ctx.fillStyle = "#f8fafc";
  ctx.font = "bold 18px 'Plus Jakarta Sans', sans-serif";
  ctx.fillText("MÔ HÌNH PHÙ HỢP NHẤT:", 80, 420);

  ctx.fillStyle = arch.primaryColor;
  ctx.font = "bold 16px 'Plus Jakarta Sans', sans-serif";
  ctx.fillText(arch.bestModel, 90, 455);

  // Footer Branding
  ctx.fillStyle = "#64748b";
  ctx.font = "14px 'Plus Jakarta Sans', sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("Khám phá lộ trình kiếm tiền 0đ tại: huyhoang2k5.github.io/solopreneur-kit", 300, 545);
}

function downloadResultImage() {
  const canvas = document.getElementById("result-canvas");
  const link = document.createElement("a");
  link.download = `AI_Archetype_${currentResultArchetype ? currentResultArchetype.title.replace(/\s+/g, '_') : 'Profile'}.png`;
  link.href = canvas.toDataURL("image/png");
  link.click();
}

function restartQuiz() {
  currentQuestionIndex = 0;
  for (const k of Object.keys(scores)) scores[k] = 0;
  document.getElementById("result-screen").classList.add("hidden");
  document.getElementById("quiz-screen").classList.remove("hidden");
  renderQuestion();
}

// Payment Modal Logic
function openQuizCheckout() {
  currentMemo = "QUIZ_" + Math.floor(1000 + Math.random() * 9000);
  document.getElementById("quiz-memo").innerText = currentMemo;

  const qrUrl = `https://img.vietqr.io/image/970423-20058999999-compact2.png?amount=19000&addInfo=${encodeURIComponent(currentMemo)}&accountName=TPBANK`;
  document.getElementById("quiz-qr-image").src = qrUrl;

  document.getElementById("checkout-modal").classList.remove("hidden");
}

function closeQuizCheckout() {
  document.getElementById("checkout-modal").classList.add("hidden");
}

function verifyQuizPayment() {
  const code = document.getElementById("quiz-tx-code").value.trim();
  if (!code || code.length < 5) {
    alert("Vui lòng nhập Mã giao dịch ngân hàng hợp lệ sau khi chuyển khoản 19.000 VNĐ.");
    return;
  }

  // Trigger download of premium report
  alert("Xác nhận thành công! Báo cáo chuyên sâu đang được tải về.");
  window.location.href = "../assets/ai_solopreneur_full_premium.pdf";
  closeQuizCheckout();
}
