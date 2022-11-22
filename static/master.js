$('.c-one').owlCarousel({
   loop: true,
   nav: false,
   autoplay: true,
   autoplayTimeout: 3000,
   autoplayHoverPause: true,
   responsive: {
      0: {
         items: 1
      },
      600: {
         items: 1
      },
      1000: {
         items: 1
      }
   }
});
$('.c-two').owlCarousel({
   loop: true,
   nav: false,
   autoplay: true,
   autoplayTimeout: 1000,
   autoplayHoverPause: true,
   responsive: {
      0: {
         items: 1
      },
      600: {
         items: 2
      },
      1000: {
         items: 5
      }
   }
});

class CountUp {
   constructor(triggerEl, counterEl) {
      const counter = document.querySelector(counterEl)
      const trigger = document.querySelector(triggerEl)
      let num = 0

      const countUp = () => {
         if (num <= counter.dataset.stop)
            ++num
         counter.textContent = num
      }

      const observer = new IntersectionObserver((el) => {
         if (el[0].isIntersecting) {
            const interval = setInterval(() => {
               (num < counter.dataset.stop) ? countUp(): clearInterval(interval)
            }, counter.dataset.speed)
         }
      }, {
         threshold: [0]
      })

      observer.observe(trigger)
   }
}


new CountUp('#start1', '#counter1')
new CountUp('#start1', '#counter2')
new CountUp('#start1', '#counter3')
new CountUp('#start1', '#counter4')
new CountUp('#start1', '#counter5')
new CountUp('#start1', '#counter6')
new CountUp('#start1', '#counter7')