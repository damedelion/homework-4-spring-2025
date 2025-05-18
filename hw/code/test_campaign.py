import time

from base import BaseCase

class TestCampaign(BaseCase):
    def test_create_campaign_site(self, campaign_page):
        url = "https://github.com/damedelion/homework-4-spring-2025"
        budget = "123"

        campaign_page.click_create_btn()
        campaign_page.click_site_field()
        campaign_page.fill_site_url_field(url)
        campaign_page.click_budget_field()
        campaign_page.fill_budget_field(budget)
        campaign_page.choose_date()

        campaign_page.click_continue_btn()
        expected_url = "https://ads.vk.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form"
        campaign_page.wait_redirect(expected_url)
        got_url = campaign_page.driver.current_url
        assert(got_url.startswith(expected_url))

    def test_create_campaign_invalid_url(self, campaign_page):
        url = "wrong url"

        campaign_page.click_create_btn()
        campaign_page.click_site_field()
        campaign_page.fill_site_url_field(url)
        campaign_page.click_continue_btn()

        expected_url_err_msg = "Не удалось подгрузить данные ссылки"
        got_err_msg = campaign_page.get_error_message()
        assert(got_err_msg == expected_url_err_msg)

    def test_create_campaign_change_name(self, campaign_page):
        new_name = "Test campaign"

        campaign_page.click_create_btn()
        campaign_page.change_name(new_name)

        got_name = campaign_page.get_name()
        assert(got_name == new_name)

    def test_create_campaign_cancel_btn(self, campaign_page):
        url = "https://github.com/damedelion/homework-4-spring-2025"
        budget = "123"

        campaign_page.click_create_btn()
        campaign_page.click_site_field()
        campaign_page.fill_site_url_field(url)
        campaign_page.click_budget_field()
        campaign_page.fill_budget_field(budget)
        campaign_page.choose_date()

        campaign_page.click_continue_btn()
        campaign_page.click_cancel_btn()

        expected_url = 'https://ads.vk.com/hq/new_create/ad_plan'
        campaign_page.wait_redirect(expected_url)
        got_url = campaign_page.driver.current_url
        assert(got_url.startswith(expected_url))

    def test_create_campaign_create_group(self, campaign_page):
        url = "https://github.com/damedelion/homework-4-spring-2025"
        budget = "123"

        campaign_page.click_create_btn()
        campaign_page.click_site_field()
        campaign_page.fill_site_url_field(url)
        campaign_page.click_budget_field()
        campaign_page.fill_budget_field(budget)
        campaign_page.choose_date()

        campaign_page.click_continue_btn()
        campaign_page.choose_region()
        campaign_page.click_continue_btn()

        expected_url = 'ad/new-ad-form_'
        campaign_page.wait_redirect(expected_url)
        got_url = campaign_page.driver.current_url
        assert(expected_url in got_url)

    def test_create_campaign_create_form(self, campaign_page):
        url = "https://github.com/damedelion/homework-4-spring-2025"
        budget = "123"
        title = "Test title"
        desc = "Test description"
        new_name = "Test campaign"

        campaign_page.click_create_btn()
        campaign_page.change_name(new_name)
        campaign_page.click_site_field()
        campaign_page.fill_site_url_field(url)
        campaign_page.click_budget_field()
        campaign_page.fill_budget_field(budget)
        campaign_page.choose_date()

        campaign_page.click_continue_btn()
        campaign_page.choose_region()
        campaign_page.click_continue_btn()

        campaign_page.fill_ad_title(title)
        campaign_page.fill_ad_short_desc(desc)
        campaign_page.choose_default_media()
        campaign_page.wait_media_generation()
        campaign_page.click_submit_btn()

        expected_url = 'https://ads.vk.com/hq/dashboard'
        campaign_page.wait_redirect(expected_url)
        got_url = campaign_page.driver.current_url
        assert(got_url.startswith(expected_url))

        # удаляем для консистентности
        campaign_page.choose_option('Удалить')
        assert(campaign_page.check_no_campaigns())
