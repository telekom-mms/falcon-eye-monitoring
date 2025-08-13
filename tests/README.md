# Tests Cases
A short description of a small suite of basic integration tests.
Goals of the tests are to check...
- components deployment
- components are successfully stacked together

<!-- TOC -->
* [Demoapp](#Demoapp)
* [F.E.M.](#F.E.M.)
* [Shellexporter](#Shellexporter)



## Demoapp
First open the Demoapp and generate some requests by clicking dedicated buttons.

| test case               | test steps                                                             | expected result      |
|-------------------------|------------------------------------------------------------------------|----------------------|
| test_owners_page        | - click on 'owners page' <br> - search for dedicated owners            | objects exist        |
| test_owners_actions     | - click on 'owners page' <br> - click on details for a dedicated owner | detail object exist  |
| test_owner_edit         | - click on 'owners page' <br> - edit dedicated owner                   | owner's data updated |
| test_owner_add          | - click on 'owners page' <br> - add dedicated owner                    | new owner added      |
| test_pet_add            | - click on 'owners page' <br> - add dedicated pet                      | new pet added        |
| test_veterinarians_page | - click on 'veterinarians page'                                        | objects exist        |
| test_raise_error        | - click on 'error' button                                              | error is raised      |

## F.E.M.
Next is to login to Grafana and check it's provisioning by search for dedicated dashboards and panels.
Further there should be found some data inside the panels.

| test case                            | test steps                                                                                      | expected result |
|--------------------------------------|-------------------------------------------------------------------------------------------------|-----------------|
| test_dashboard_contains_panels       | - click on dashboard 'demoapp'                                                                  | object exists   |
| test_panel_data_trace_duration_graph | - click on dashboard 'demoapp'<br> - check existing panel by heading <br> - check panel content | content exists  |
| test_panel_data_trace_duration_list  | - click on dashboard 'demoapp'<br> - check existing panel by heading <br> - check panel content | content exists  |
| test_panel_data_runtime_exception    | - click on dashboard 'demoapp'<br> - check existing panel by heading <br> - check panel content | content exists  |
| test_panel_data_http_status          | - click on dashboard 'demoapp'<br> - check existing panel by heading <br> - check panel content | content exists  |
| test_panel_data_app_starts           | - click on dashboard 'demoapp'<br> - check existing panel by heading <br> - check panel content | content exists  |

## Shellexporter
Last there should be a panel and inside some data for the shellexporter as well.

| test case                     | test steps                                                                | expected result |
|-------------------------------|---------------------------------------------------------------------------|-----------------|
| test_dashboards_exists        | - click on dashboard 'shellexporter'                                      | object exists   |
| test_dashboard_contains_panel | - click on dashboard 'shellexporter' <br> - search for dedicated panel    | object exists   |
| test_panel                    | - click on dashboard 'shellexporter' <br> - search for dedicated diagram  | objects exist   |