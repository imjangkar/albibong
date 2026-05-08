import React, { createContext, useContext, useState } from "react";
import zhTranslations from "../locales/zh.json";
import enTranslations from "../locales/en.json";

export type Locale = "en" | "zh";

type TranslationKeys = typeof zhTranslations;

const translations: Record<Locale, TranslationKeys> = {
  en: enTranslations,
  zh: zhTranslations,
};

interface I18nContextValue {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: (key: string, params?: Record<string, string | React.ReactNode>) => string;
}

const I18nContext = createContext<I18nContextValue | null>(null);

export const I18nProvider = ({ children }: { children: React.ReactNode }) => {
  const [locale, setLocale] = useState<Locale>("en");

  const t = (key: string, params?: Record<string, string | React.ReactNode>): string => {
    const keys = key.split(".");
    let value: unknown = translations[locale];
    for (const k of keys) {
      if (value && typeof value === "object" && k in value) {
        value = (value as Record<string, unknown>)[k];
      } else {
        return key;
      }
    }
    if (typeof value !== "string") return key;

    if (params) {
      return value.replace(/\{(\w+)\}/g, (_, paramKey) => {
        return params[paramKey]?.toString() ?? `{${paramKey}}`;
      });
    }
    return value;
  };

  return (
    <I18nContext.Provider value={{ locale, setLocale, t }}>
      {children}
    </I18nContext.Provider>
  );
};

export const useI18n = () => {
  const context = useContext(I18nContext);
  if (!context) throw new Error("useI18n must be used within I18nProvider");
  return context;
};
