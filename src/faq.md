# FAQ

<dl>
<dt>Can I use CWL and cwltool with Singularity?</dt>
<!-- https://matrix.to/#/!RQMxrGNGkeDmWHOaEs:gitter.im/$f1B-ytoep4PX3_tTgxaADRQFHGgisGiUL1nUHVQPBnY?via=gitter.im&via=matrix.org&via=gottliebtfreitag.de -->
<dd>The CWL standards are built around (optional) Docker format containers.
The reference runner and several other CWL implementations support running
those Docker format containers using the Singularity engine. Directly
specifying a Singularity format container is not part of the CWL standards.</dd>
</dl>

% - https://github.com/common-workflow-language/user_guide/issues/6
% - Maybe adapt some of these (or move to a workaround?) https://www.synapse.org/#!Synapse:syn2813589/wiki/401464
