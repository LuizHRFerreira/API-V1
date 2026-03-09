import { test, expect } from '@playwright/test'

test('homepage has title and links', async ({ page }) => {
  await page.goto('/')

  await expect(page).toHaveTitle(/API Front/)

  await expect(page.getByRole('heading', { level: 1 })).toContainText('API Front')

  await expect(page.getByRole('link', { name: 'Home' })).toBeVisible()
  await expect(page.getByRole('link', { name: 'Dashboard' })).toBeVisible()
  await expect(page.getByRole('link', { name: 'Sobre' })).toBeVisible()
})

test('navigation to about page', async ({ page }) => {
  await page.goto('/')

  await page.getByRole('link', { name: 'Sobre' }).click()

  await expect(page).toHaveURL('/about')

  await expect(page.getByRole('heading', { level: 2 })).toContainText('Sobre')
})