const metrics = [
  { label: "Protein", value: "112g", tone: "P" },
  { label: "Fat", value: "48g", tone: "F" },
  { label: "Carbs", value: "210g", tone: "C" },
];

const meals = [
  { name: "Breakfast", summary: "Greek yogurt / banana / oats", pfc: "28 / 9 / 46" },
  { name: "Lunch", summary: "Chicken bowl / rice / greens", pfc: "41 / 14 / 63" },
  { name: "Dinner", summary: "Salmon / potatoes / salad", pfc: "43 / 21 / 38" },
];

export default function Home() {
  return (
    <main
      style={{
        padding: "40px 20px 72px",
      }}
    >
      <section
        style={{
          maxWidth: 1080,
          margin: "0 auto",
          display: "grid",
          gap: 24,
        }}
      >
        <div
          style={{
            display: "grid",
            gap: 16,
            padding: 28,
            border: "1px solid var(--border)",
            borderRadius: 28,
            background: "var(--panel)",
            backdropFilter: "blur(14px)",
            boxShadow: "0 24px 60px rgba(38, 29, 18, 0.08)",
          }}
        >
          <span
            style={{
              width: "fit-content",
              padding: "6px 10px",
              borderRadius: 999,
              background: "rgba(201, 111, 59, 0.12)",
              color: "var(--accent-strong)",
              fontSize: 13,
              fontWeight: 700,
              letterSpacing: "0.04em",
            }}
          >
            SMALL START
          </span>
          <div style={{ display: "grid", gap: 8 }}>
            <h1 style={{ margin: 0, fontSize: "clamp(2.5rem, 7vw, 4.8rem)", lineHeight: 0.94 }}>
              Meal-by-meal
              <br />
              PFC balance
            </h1>
            <p style={{ margin: 0, maxWidth: 680, color: "var(--muted)", fontSize: 18, lineHeight: 1.6 }}>
              食事ごとにタンパク質、脂質、炭水化物を記録して、1日のバランスを気持ちよく追える最小構成のスタート画面です。
            </p>
          </div>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
            gap: 16,
          }}
        >
          {metrics.map((metric) => (
            <article
              key={metric.label}
              style={{
                padding: 22,
                borderRadius: 24,
                border: "1px solid var(--border)",
                background: "rgba(255, 255, 255, 0.72)",
              }}
            >
              <div style={{ color: "var(--muted)", fontSize: 14 }}>{metric.label}</div>
              <div style={{ marginTop: 14, fontSize: 36, fontWeight: 700 }}>{metric.value}</div>
              <div style={{ marginTop: 8, color: "var(--accent-strong)", fontWeight: 600 }}>
                Today&apos;s {metric.tone}
              </div>
            </article>
          ))}
        </div>

        <section
          style={{
            display: "grid",
            gridTemplateColumns: "2fr 1fr",
            gap: 16,
          }}
        >
          <div
            style={{
              padding: 24,
              borderRadius: 28,
              border: "1px solid var(--border)",
              background: "rgba(255, 252, 248, 0.9)",
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 12 }}>
              <h2 style={{ margin: 0, fontSize: 24 }}>Meals</h2>
              <span style={{ color: "var(--muted)", fontSize: 14 }}>P / F / C</span>
            </div>
            <div style={{ display: "grid", gap: 14, marginTop: 18 }}>
              {meals.map((meal) => (
                <article
                  key={meal.name}
                  style={{
                    padding: 18,
                    borderRadius: 18,
                    border: "1px solid var(--border)",
                    background: "#fffdf8",
                  }}
                >
                  <div style={{ display: "flex", justifyContent: "space-between", gap: 16 }}>
                    <strong>{meal.name}</strong>
                    <span style={{ color: "var(--accent-strong)", fontWeight: 700 }}>{meal.pfc}</span>
                  </div>
                  <p style={{ margin: "10px 0 0", color: "var(--muted)" }}>{meal.summary}</p>
                </article>
              ))}
            </div>
          </div>

          <aside
            style={{
              padding: 24,
              borderRadius: 28,
              border: "1px solid var(--border)",
              background: "#2f2418",
              color: "#fff6ec",
            }}
          >
            <h2 style={{ marginTop: 0, fontSize: 24 }}>Next Step</h2>
            <p style={{ color: "rgba(255, 246, 236, 0.76)", lineHeight: 1.7 }}>
              次は meal 登録フォーム、日次集計 API、PostgreSQL 永続化を順に追加していく想定です。
            </p>
            <div
              style={{
                marginTop: 24,
                padding: 16,
                borderRadius: 20,
                background: "rgba(255, 255, 255, 0.08)",
              }}
            >
              <div style={{ fontSize: 13, letterSpacing: "0.04em", opacity: 0.8 }}>API Target</div>
              <div style={{ marginTop: 8, fontSize: 18, fontWeight: 700 }}>/api/v1/meals</div>
            </div>
          </aside>
        </section>
      </section>
    </main>
  );
}
