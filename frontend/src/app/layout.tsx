import type { Metadata } from "next";
import "./globals.css";
import { DeterminexErrorBoundary } from "@/components/DeterminexErrorBoundary";
import { IterationThemeProvider } from "@/contexts/IterationThemeContext";
import { SettingsProvider } from "@/contexts/SettingsContext";
import { AiRouterProvider } from "@/contexts/AiRouterContext";
import { ToastProvider } from "@/components/ErrorToast";

export const metadata: Metadata = {
  title: "Determinex — AI Pack Orchestration Platform",
  description:
    "A local-first, multi-model AI orchestration IDE for autonomous code generation, context management, and pack-based reasoning.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning className="h-full antialiased">
      <body className="min-h-full flex flex-col">
        <IterationThemeProvider>
          <ToastProvider>
            <SettingsProvider>
              <AiRouterProvider>
                <DeterminexErrorBoundary>{children}</DeterminexErrorBoundary>
              </AiRouterProvider>
            </SettingsProvider>
          </ToastProvider>
        </IterationThemeProvider>
      </body>
    </html>
  );
}
