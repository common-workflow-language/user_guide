# FAQ

<dl>
<dt>Can I use CWL and cwltool with Singularity?</dt>
<!-- https://matrix.to/#/!RQMxrGNGkeDmWHOaEs:gitter.im/$f1B-ytoep4PX3_tTgxaADRQFHGgisGiUL1nUHVQPBnY?via=gitter.im&via=matrix.org&via=gottliebtfreitag.de -->
<dd>The CWL standards are built around (optional) Docker format containers.
The reference runner and several other CWL implementations support running
those Docker format containers using the Singularity engine. Directly
specifying a Singularity format container is not part of the CWL standards.</dd>

<dt>How can I debug JavaScript expressions?</dt>
<dd>You can use the <code>--js-console</code> option of <code>cwltool</code>, or you can try
creating a JavaScript or TypeScript project for your code, and load it
using <code>expressionLib</code>, e.g.: <a href="https://github.com/common-workflow-language/common-workflow-language/blob/master/v1.0/v1.0/template-tool.cwl#L6-L8">
https://github.com/common-workflow-language/common-workflow-language/blob/master/v1.0/v1.0/template-tool.cwl#L6-L8</a></dd>
</dl>

% - https://github.com/common-workflow-language/user_guide/issues/6
% - Maybe adapt some of these (or move to a workaround?) https://www.synapse.org/#!Synapse:syn2813589/wiki/401464
