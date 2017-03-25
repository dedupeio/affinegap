#!/usr/bin/env bash

set -e -x

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    if [[ "${PYBIN}" == *"cp27"* ]] || [[ "${PYBIN}" == *"cp34"* ]] || [[ "${PYBIN}" == *"cp35"* ]] || [[ "${PYBIN}" == *"cp36"* ]]; then
        "${PYBIN}/pip" install -r /io/requirements.txt
        "${PYBIN}/cython" /io/affinegap/*.pyx
        "${PYBIN}/pip" install -e /io/
        "${PYBIN}/pip" wheel /io/ -w wheelhouse/
    fi
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/affinegap*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/*/bin; do
    if [[ "${PYBIN}" == *"cp27"* ]] || [[ "${PYBIN}" == *"cp34"* ]] || [[ "${PYBIN}" == *"cp35"* ]] || [[ "${PYBIN}" == *"cp36"* ]]; then
        "${PYBIN}/pip" uninstall -y affinegap
        "${PYBIN}/pip" install affinegap --no-index -f /io/wheelhouse
        "${PYBIN}/pytest" /io/tests
    fi
done

