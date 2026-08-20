// ============================================================
// OS - Obras & Serviços | Header JS v2
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.header');
  
  // Efeito de background do header ao fazer scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.style.backgroundColor = 'rgba(14, 15, 16, 0.95)';
      header.style.backdropFilter = 'blur(10px)';
    } else {
      header.style.backgroundColor = 'transparent';
      header.style.backdropFilter = 'none';
    }
  });

  // Mobile menu toggle (demonstrativo)
  const mobileBtn = document.querySelector('.header__mobile-btn');
  if (mobileBtn) {
    mobileBtn.addEventListener('click', () => {
      // Para esta etapa, apenas um alert ou console, já que o menu não foi desenhado
      console.log('Mobile menu click');
    });
  }
});
