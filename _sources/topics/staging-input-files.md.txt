# Staging input files

Normally, input files are located in a read-only directory separate from
the output directory.  This causes problems if the underlying tool expects to
write its output files alongside the input file in the same directory.  You use `InitialWorkDirRequirement` to stage input files into the output directory.
In this example, we use a JavaScript expression to extract the base name of the
input file from its leading directory path.

```{literalinclude} /_includes/cwl/staging-input-files/linkfile.cwl
:language: cwl
:caption: "`linkfile.cwl`"
:name: linkfile.cwl
```

```{literalinclude} /_includes/cwl/staging-input-files/arguments-job.yml
:language: yaml
:caption: "`arguments-job.yml`"
```

Now invoke `cwltool` with the tool description and the input object on the
command line:

```{runcmd} cwltool linkfile.cwl arguments-job.yml
:working-directory: src/_includes/cwl/staging-input-files/
```
