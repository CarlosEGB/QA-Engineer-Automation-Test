from behave import when, use_step_matcher

from lib.components.generalcomponents import GeneralComponents
from lib.helpers.generalhelpers import transformation_helper
from lib.pages.webelements.homewebelements import option_menu_right

use_step_matcher("re")


@when(u'I click on the "(?P<element_name>.*)" "(?P<element_type>button|dropdown|option)"')
def step_impl(context, element_name, element_type):
    element_name = transformation_helper(element_name, element_type)
    if GeneralComponents.wait_until_element_is_clickable(
            context, context.current_page.webElements.__dict__.get(element_name)
    ):
        return context.browser.find_element(context.current_page.webElements.__dict__.get(element_name)).click()


@when(u'I navigate to the "(?P<url>.*)" URL')
def step_impl(context, url):
    return context.browser.visit(url)


@when('I select "(?P<option>.*)" in the dropdown')
def step_impl(context, option):
    return context.current_page.text_value_in_the_select(option)


@when(u'I search "(?P<option>.*)" in the input')
def step_impl(context, option):
    return context.current_page.text_value_in_the_filter(option)


@when(u'I navigate each of the right menu "(?P<option>.*)"')
def step_impl(context, option):
    if GeneralComponents.wait_until_element_is_clickable(
            context, context.browser.find_element(option_menu_right(option))
    ):
        return context.browser.find_element(option_menu_right(option)).click()
