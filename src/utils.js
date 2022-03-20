function scrapeHtmlElementsList(listContainer) {
  const listItemNodes = listContainer.querySelectorAll("li");
  const listItemsArray = Array.from(listItemNodes);

  const data = [];

  for (li of listItemsArray) {
    const dataItem = {};
    dataItem.name = li.querySelector("code").textContent.replace(/[\<\>]/g, "");

    if (isDeprecated(li)) {
      dataItem.deprecated = true;
    }

    if (isNonStandard(li)) {
      dataItem.nonStandard = true;
    }

    if (isExperimental(li)) {
      dataItem.experimental = true;
    }

    data.push(dataItem);
  }

  return JSON.stringify(data);

  function isDeprecated(listItem) {
    const hasDeprecatedIcon = Boolean(listItem.querySelector(".icon-deprecated"));

    return hasDeprecatedIcon;
  }

  function isNonStandard(listItem) {
    const hasNonStandardIcon = Boolean(listItem.querySelector(".icon-nonstandard"));

    return hasNonStandardIcon;
  }

  function isExperimental(listItem) {
    const hasExperimentalIcon = Boolean(listItem.querySelector(".icon-experimental"));

    return hasExperimentalIcon;
  }
}
