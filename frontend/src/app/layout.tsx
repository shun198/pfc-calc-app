import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PFC Meal Balance",
  description: "Track protein, fat, and carbs meal by meal.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
