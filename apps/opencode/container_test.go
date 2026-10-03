package main

import (
	"testing"

	"github.com/chaijunkin/containers/testhelpers"
)

func Test(t *testing.T) {
	image := testhelpers.GetTestImage("ghcr.io/chaijunkin/opencode:rolling")
	testhelpers.TestCommandSucceeds(t, image, nil, "/usr/local/bin/opencode", "--version")
	testhelpers.TestCommandSucceeds(t, image, nil, "/usr/bin/git", "--version")
	testhelpers.TestCommandSucceeds(t, image, nil, "/usr/bin/gh", "--version")
}
