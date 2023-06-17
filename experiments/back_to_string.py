import urllib.parse


def main(data: str):
    new_string = data.replace("{", "(").replace("[", "(").replace("]", ")").replace(" ", "")

    print(new_string)


if __name__ == "__main__":
    main(
        "[{'facetSelections': ['List', [{'type': 'SOURCING_CHANNEL'}, {'valuesWithSelections': 'List'}], [{'type': 'CANDIDATE_HIRING_STATE'}, {'valuesWithSelections': ['List', [{'value': 'urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771247229)'}, {'selected': 'true'}, {'selected': 'false'}, {'required': 'false'}], [{'value': 'urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771251051)'}, {'selected': 'true'}, {'negated': 'false'}, {'required': 'false'}], [{'value': 'urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771252348)'}, {'selected': 'true'}, {'negated': 'false'}, {'required': 'false'}], [{'value': 'urn:li:ts_hiring_state:(urn:li:ts_contract:454254206,12771251050)'}, {'selected': 'true'}, {'negated': 'false'}, {'required': 'false'}]]}]]}, {'capSearchSortBy': 'HIRING_CANDIDATE_LAST_UPDATED_DATE'}, {'hiringProjects': ['List', [{'text': 'python'}, {'entity': 'urn:li:ts_hiring_project:(urn:li:ts_contract:454254206,1042246722)'}]]}]"
    )
