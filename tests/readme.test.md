<!--PIPELINE_DOCS-->
<b>Pipeline worflow</b>
<table>
<tr><th>Pipeline name</th><th>Trigger</th><th>Variable</th><th>Default value</th><th>Required</th><th>Type</th><th>Choices</th></tr>
<tr><td rowspan="3">Deployment to $ENV</td><td rowspan="3"><b>if:</b> $CI_PIPELINE_SOURCE == 'web'</td><td>ENV</td><td>none</td><td>Yes</td><td>-</td><td>dev, prod, test</td></tr><tr><td>ACC_ID</td><td>None</td><td>Yes</td><td>str</td><td>-</td></tr>
<tr><td>LOG_LEVEL</td><td>debug</td><td>No</td><td>-</td><td>info, critical, error, debug</td></tr>
<tr><td rowspan="2">hmm</td><td rowspan="2"><b>if:</b> $CI_PIPELINE_SOURCE == 'api' || $CI_COMMIT_BRANCH == 'main'</td><td>ENV</td><td>stage</td><td>Yes</td><td>-</td><td>dev, prod, test</td></tr><tr><td>ACC_ID</td><td>None</td><td>Yes</td><td>str</td><td>-</td></tr>
<tr><td></td><td><b>if:</b> $CI_COMMIT_BRANCH != 'main'<br><b>when:</b> never</td></tr>
<tr><td></td><td><b>if:</b> $CI_COMMIT_TAG</td><td>ENV</td><td>bla</td></tr>
<tr><td></td><td><b>when:</b> never</td></tr>
</table>
<b>Global variables</b>
<table>
<tr><th>Name</th><th>Value</th><th>Required</th><th>Type</th><th>Choices</th></tr>
<tr><td>AWS_ACC_ID</td><td>123456789</td></tr>
<tr><td>ENV</td><td>dev</td><td>Yes</td><td>-</td><td>stage, test</td></tr>
</table>
<!--PIPELINE_DOCS-->

## This is test

asldpasldpasdl aspdl pasld pasld pasldp l

### some list
- asd
- wer
- asd
    - 2345

### sdf
sdf sdf
<br>dsf sdfdsf sdf sdf dsf sdf
