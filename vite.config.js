import { defineConfig } from "vite";

export default defineConfig({
  appType: "mpa",
  server: {
    host: "0.0.0.0",
    port: 43123,
    strictPort: true,
  },
});
