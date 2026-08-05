import sys
import re

file_path = r'c:\Users\onell\OneDrive\Desktop\SiteLab India\SiteLab-India-main\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Edit 1
content = content.replace(
    '<meta name="description" content="Kota mein professional website chahiye? SiteLab India — 72 ghante mein ready, ₹1,499 se shuru. Doctors, clinics, gyms, hostels, photographers, resorts, salons, cafes ke liye. Demo free, payment baad mein. Call: 7878574692">',
    '<meta name="description" content="Kota mein professional website chahiye? SiteLab India — custom quotation, free demo pehle. Doctors, clinics, gyms, hostels, photographers, resorts ke liye websites banate hain. Payment sirf approval ke baad. Call: 7878574692">'
)

# Edit 2
lines = content.split('\n')
lines = [l for l in lines if '"priceRange": "₹₹",' not in l]
content = '\n'.join(lines)

# Edit 3
content = content.replace(
    '<a href="#getstarted" class="nav-cta">Get Free Strategy</a>',
    '<a href="#getstarted" class="nav-cta">Get Free Quotation</a>'
)

# Edit 4
content = content.replace(
    'Doctors, Clinics, Gyms, Hostels, Food Businesses, Photographers, Resorts &amp; Hotels — 72 ghante mein live, demo pehle, payment baad mein.',
    'Doctors, Clinics, Gyms, Hostels, Food Businesses, Photographers, Resorts &amp; Hotels — demo pehle, payment baad mein, poori website aapke business ke hisaab se custom.'
)

# Edit 5
content = content.replace(
    '72-hour delivery',
    '100% Custom-Built Websites',
    1
)

# Edit 6
content = content.replace(
    '<h4>72-Hour Express Delivery</h4>\n        <p>From approval to public launch</p>',
    '<h4>Custom Quotation</h4>\n        <p>Pricing tailored to your business</p>'
)

# Edit 7
content = re.sub(
    r'<!-- ===== PRICING SECTION ===== -->.*?<!-- ===== END PRICING SECTION ===== -->',
    '''<!-- ===== SERVICES SECTION ===== -->
<section id="pricing" class="pricing-section">
  <div class="container">
    <div class="section-eyebrow">Our Services</div>
    <h2 class="section-title">Hum Kya Banate Hain</h2>
    <p class="section-subtitle">Har business alag hota hai — isliye har website bhi custom hoti hai. Exact scope aapke requirement pe depend karta hai. Neeche dekho hum kya deliver karte hain, phir free quotation ke liye WhatsApp karo.</p>

    <div class="pricing-grid">

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--basic">🌐 Single Page Website</div>
          <div class="plan-tagline" style="margin-top:16px;">Ek professional single-page website jo turant online le aaye. WhatsApp integration, mobile-responsive, Google pe visible.</div>
        </div>
      </div>

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--popular">📄 Multi-Page Website</div>
          <div class="plan-tagline" style="margin-top:16px;">Bade business ke liye — Home, About, Services, Gallery, Contact — sab alag pages ke saath poora digital presence.</div>
        </div>
      </div>

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--premium">🌍 Custom Domain + Business Email</div>
          <div class="plan-tagline" style="margin-top:16px;">Apna khud ka domain (yourbusiness.in) aur professional email — apni pehchaan, apna brand.</div>
        </div>
      </div>

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--basic">🔍 Local SEO &amp; Google Business Setup</div>
          <div class="plan-tagline" style="margin-top:16px;">Google Maps, Google Business Profile, aur local SEO — taaki Kota mein customers aapko dhoondh saken.</div>
        </div>
      </div>

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--popular">🔧 Monthly Care &amp; Maintenance</div>
          <div class="plan-tagline" style="margin-top:16px;">Ongoing updates aur technical support, chhoti monthly fee mein — poora control aapke paas.</div>
        </div>
      </div>

      <div class="pricing-card">
        <div class="pricing-card-inner">
          <div class="plan-badge plan-badge--premium">📈 SEO Growth Plan</div>
          <div class="plan-tagline" style="margin-top:16px;">Already website hai? Sirf SEO aur Google ranking pe kaam karte hain — monthly optimization.</div>
        </div>
      </div>

    </div>

    <div style="text-align: center; margin-top: 40px;">
      <a href="#getstarted" class="plan-cta plan-cta--primary" style="display: inline-block; padding: 16px 40px; font-size: 1.1rem;">📲 Get Free Quotation</a>
    </div>

    <!-- Guarantee strip -->
    <div class="pricing-guarantee">
      <span class="guarantee-icon">🔒</span>
      <p><strong>Zero-Risk Guarantee:</strong> You only pay after you see and approve your completed website. If you don't love it, you don't pay — no questions asked.</p>
    </div>

  </div>
</section>
<!-- ===== END SERVICES SECTION ===== -->''',
    content,
    flags=re.DOTALL
)

# Edit 8
content = content.replace(
    '"72 ghante mein poori website ready. Demo bilkul waisa tha jaisa maingne socha tha. Payment ke baad koi tension nahi — seedha live ho gayi."',
    '"Website bilkul waisa hi bani jaisa maine socha tha. Payment ke baad koi tension nahi — seedha live ho gayi."'
)

# Edit 9
content = content.replace(
    '<span class="stat-num">72hr</span>\n            <span class="stat-label">Avg. Delivery</span>',
    '<span class="stat-num">Free</span>\n            <span class="stat-label">Custom Quotation</span>'
)

# Edit 10
content = content.replace(
    'Quick Launch package mein 24 ghante, Professional aur Business mein 72 ghante, aur Premium multi-page mein 5-7 din. Demo approval ke baad timer start hota hai.',
    'Timeline aapki website ki requirement pe depend karta hai — quotation ke time hi exact timeline confirm ho jaayega. Hum fast turnaround pe kaam karte hain, bina quality compromise kiye.'
)

# Edit 11
content = content.replace(
    'Quick Launch aur Professional mein domain included nahi hai (GitHub Pages free URL milta hai). Business package (₹4,999) aur usse upar mein 1 saal ka custom domain included hai.',
    'Depends on plan. Kuch websites free hosting URL pe hoti hain, kuch mein custom domain bhi included hota hai. Quotation ke time discuss kar lenge ki aapke liye kya best rahega.'
)

# Edit 12
content = content.replace(
    'Nahi. Hum GitHub Pages ya similar free platform use karte hain — no monthly hosting charge. Sirf Business/Premium mein domain renewal cost hogi (approx ₹800/year).',
    'Hosting free hai — koi monthly charge nahi. Custom domain lo toh sirf uska yearly renewal cost hota hai (domain provider ko jaata hai) — quotation mein clear kar denge.'
)

# Edit 13
content = content.replace(
    'Haan. Aap khud WhatsApp pe changes bhej sakte ho — hum update kar dete hain. Ya humara Monthly Plan (Growth/Pro) le sakte ho jisme regular updates included hote hain. Sirf Google ranking badhani ho toh SEO Care plan (₹799/month) alag se hai.',
    'Haan, WhatsApp pe changes bhejo, hum update kar dete hain. Regular updates ke liye Monthly Care Plan hai, SEO ke liye SEO Growth Plan — quotation ke time detail bata denge.'
)

# Edit 14
content = content.replace(
    '<h2 class="section-title">Get Your Free Website Strategy</h2>',
    '<h2 class="section-title">Get Your Free Quotation</h2>'
)

# Edit 15
content = content.replace(
    'Request Your <span style="color: var(--gold);">Free Website Strategy</span>',
    'Request Your <span style="color: var(--gold);">Free Quotation</span>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Edits done")
