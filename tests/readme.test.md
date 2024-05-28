<!--PIPELINE_DOCS-->
<table>
<tr><th>Pipeline name</th><th>Trigger</th><th>Variable</th><th>Default value</th><th>Required</th><th>Type</th><th>Choices</th></tr>
<tr><td rowspan="3"></td><td rowspan="3"><b>if:</b> $CI_PIPELINE_SOURCE == 'web'</td><td>ENV</td><td>dev</td><td>No</td><td>-</td><td>dev, prod, test</td></tr><tr><td>ACC_ID</td><td>None</td><td>No</td><td>str</td><td>-</td></tr>
<tr><td>MODE</td><td>bla</td><td>Yes</td><td>-</td><td>dep, art</td></tr>
<tr><td rowspan="2">hmm</td><td rowspan="2"><b>if:</b> $CI_PIPELINE_SOURCE == 'api'</td><td>ENV</td><td>stage</td><td>Yes</td><td>-</td><td>dev, prod, test</td></tr><tr><td>ACC_ID</td><td>None</td><td>Yes</td><td>str</td><td>-</td></tr>
<tr><td></td><td><b>if:</b> $CI_COMMIT_BRANCH != 'main'<br><b>when:</b> never</td></tr>
<tr><td></td><td><b>if:</b> $CI_COMMIT_TAG</td><td>ENV</td><td>bla</td><td>No</td><td>-</td><td>-</td></tr>
<tr><td></td><td><b>when:</b> never</td></tr>
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
