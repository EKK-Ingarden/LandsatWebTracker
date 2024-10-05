import type { paths as ApiPaths } from "#open-fetch-schemas/api";

export default function apiAuth(url: keyof ApiPaths, options: any = {}) {
  const token = useSupabaseSession().value?.access_token;

  if (token) {
    options.headers = {
      ...options.headers,
      Authorization: `Bearer ${token}`
    };
  }

  return useApi(url, options);
}
